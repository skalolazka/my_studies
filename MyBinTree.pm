#!/usr/bin/perl

package MyBinTree;

use strict;
#use warnings;

sub new {
    my ($class, $val) = @_;
    return bless { value => $val, left => undef, right => undef } => $class;
}

sub put_left {
    my ($self, $val) = @_;
    if (ref($val) eq 'MyBinTree') {
        $self->{left} = $val;
    }
    else {
        $self->{left} = MyBinTree->new($val);
    }
}

sub put_right {
    my ($self, $val) = @_;
    if (ref($val) eq 'MyBinTree') {
        $self->{right} = $val;
    }
    else {
        $self->{right} = MyBinTree->new($val);
    }
}

sub inorder {
    my ($class, $t, $result) = @_;
    return $result unless defined($t);
    $result = $class->inorder($t->{left}, $result);
    push(@$result, $t->{value});
    $result = $class->inorder($t->{right}, $result);
    return $result;
}

sub preorder {
    my ($class, $t, $result) = @_;
    return $result unless defined($t); 
    push(@$result, $t->{value});
    $result = $class->preorder($t->{left}, $result);
    $result = $class->preorder($t->{right}, $result);
    return $result;
}

sub postorder {
    my ($class, $t, $result) = @_;
    return $result unless defined($t); 
    $result = $class->postorder($t->{left}, $result);
    $result = $class->postorder($t->{right}, $result);
    push(@$result, $t->{value});
    return $result;
}

sub check_subtree {
    my ($class, $t, $n, $result) = @_;
    return $result if defined($result) || !defined($t);
    if ($t == $n) {
        return $t;
    }
    else {
        $result = $class->check_subtree($t->{left}, $n, $result);
        unless (defined($result)) {
            $result = $class->check_subtree($t->{right}, $n, $result);
        }
    }
    return $result;
}


sub lca {
    my ($class, $t, $node1, $node2, $found1, $found2, $lca) = @_;
    return ($found1, $found2, $lca) unless defined($t) && defined($node1) && defined($node2);
    my @found = ($found1, $found2);
    my @node = ($node1, $node2);
    if (!$found[0] && !$found[1]) {
        if ($t == $node[0] && $t == $node[1]) {
            $lca = $t;
        }
        elsif ($t == $node[0] || $t == $node[1]) {
            my $x = $t == $node[0] ? 0 : 1;
            $found[$x] = $t;
            $found[1-$x] = $class->check_subtree($t, $node[1-$x]);
            if ($found[1-$x]) { $lca = $t }
        }
        else {
            ($found[0], $found[1], $lca) = $class->lca($t->{left}, $node[0], $node[1], $found[0], $found[1], $lca);
            unless ($lca) {
                # $found[0] && $found[1] can't be - because lca is not set
                if ($found[0] || $found[1]) {
                    my $x = $found[0] ? 0 : 1;
                    $found[1-$x] = $class->check_subtree($t->{right}, $node[1-$x]);
                    if ($found[1-$x]) { $lca = $t }
                    $found[$x] = $t;
                }
                else {
                    ($found[0], $found[1], $lca) = $class->lca($t->{right}, $node[0], $node[1], $found[0], $found[1], $lca);
                }
            }
        }
    }
    elsif ($found[0] || $found[1]) {
        # ok because checked subtrees before - so here we come from a child
        my $x = $found[0] ? 0 : 1;
        if ($found[$x] == $t->{left}) {
            if ($t == $node[1-$x]) {
                $lca = $t;
            }
            else {
                $found[1-$x] = $class->check_subtree($t->{right}, $node[1-$x]);
                if ($found[1-$x]) { $lca = $t }
            }
        }
        $found[$x] = $t;
    }
    elsif (!$lca) {
        $lca = $t;
    }
    return ($found[0], $found[1], $lca);
}

1;
