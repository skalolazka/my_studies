#!/usr/bin/perl

use strict;
use warnings;

package MyQueueFromStacks;

sub new {
    my ($class, @values) = @_;
    my $self = {
        stack1 => \@values,
        stack2 => [],
        what => 's', # status of stack1 - either stack ('s') or queue ('q')
        # stack2 is always a stack
    };
    # let us use just arrays for stacks here, I don't want
    # to rewrite the stack class again
    return bless $self => $class;
}

sub enqueue {
    my ($self, $val) = @_;
    if (!scalar(@{$self->{stack1}}) && !scalar(@{$self->{stack2}})) {
        push(@{$self->{stack1}}, $val);
    }
    elsif (!scalar(@{$self->{stack2}}) && ($self->{what} eq 's')) {
        push(@{$self->{stack1}}, $val);
    }
    elsif (!scalar(@{$self->{stack2}}) && ($self->{what} eq 'q')) {
        push(@{$self->{stack2}}, $val);
    }
    else {
        push(@{$self->{stack2}}, $val);
    }
    return $val;
}

sub dequeue {
    my $self = shift;
    my $result;
    if (!scalar(@{$self->{stack1}}) && !scalar(@{$self->{stack2}})) {
        return undef;
    }
    elsif (!scalar(@{$self->{stack2}}) && ($self->{what} eq 'q')) {
        return pop(@{$self->{stack1}});
    }
    elsif (!scalar(@{$self->{stack2}}) && ($self->{what} eq 's')) {
        my $val = pop(@{$self->{stack1}});
        while (defined($val)) {
            push(@{$self->{stack2}}, $val);
            $val = pop(@{$self->{stack1}});
        }
        $result = pop(@{$self->{stack2}});
        ($self->{stack1}, $self->{stack2}) = ($self->{stack2}, $self->{stack1});
        $self->{what} = 'q';
    }
    elsif ($self->{what} eq 's') { # 2 not empty stack, 1 stack - shouldn't happen
        warn 'dafuq';
        use Data::Dumper;
        warn Dumper($self);
    }
    elsif ($self->{what} eq 'q') { # 2 not empty stack, 1 queue
        $result = pop(@{$self->{stack1}});
        unless (scalar(@{$self->{stack1}})) {
            ($self->{stack1}, $self->{stack2}) = ($self->{stack2}, $self->{stack1});
            $self->{what} = 's';
        }
    }
    return $result;
}


package TestMyQueueFromStacks;

my $m = MyQueueFromStacks->new;

use Test::More tests => 14;

is($m->dequeue, undef, 'nothing to dequeue');
is($m->enqueue(2), 2, 'enqueued');
$m->enqueue(3);
$m->enqueue(4);
$m->enqueue(5);
is($m->dequeue, 2, 'one');
is($m->dequeue, 3, 'two');
is($m->dequeue, 4, 'three');
is($m->dequeue, 5, 'four');
is($m->dequeue, undef, 'none left');
$m->enqueue(3);
is($m->dequeue, 3, 'again');
$m = MyQueueFromStacks->new(1,2,3);
is($m->dequeue, 1, 'from full');
is($m->dequeue, 2, 'from full again');
$m->enqueue(4);
is($m->dequeue, 3, 'from full again and again');
$m->enqueue(5);
$m->enqueue(6);
$m->enqueue(7);
is($m->dequeue, 4, 'from full again and again');
is($m->dequeue, 5, 'from full again and again');
$m->enqueue(8);
is($m->dequeue, 6, 'from full again and again');

#done_testing();
