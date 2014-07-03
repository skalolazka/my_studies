#!/usr/bin/perl

use strict;
use warnings;

package MyQueueFromStacks;

sub new {
    my ($class, @values) = @_;
    my $self = {
        full_stack => \@values,
        empty_stack => [],
    };
    # let us use just arrays for stacks here, I don't want
    # to rewrite the stack class again
    return bless $self => $class;
}

sub enqueue {
    my ($self, $val) = @_;
    push(@{$self->{full_stack}}, $val);
    return $val;
}

sub dequeue {
    my $self = shift;
    return undef unless scalar(@{$self->{full_stack}});
    my $val = pop(@{$self->{full_stack}});
    while (defined($val)) {
        push(@{$self->{empty_stack}}, $val);
        $val = pop(@{$self->{full_stack}});
    }
    my $result = pop(@{$self->{empty_stack}});
    $val = pop(@{$self->{empty_stack}});
    while (defined($val)) {
        push(@{$self->{full_stack}}, $val);
        $val = pop(@{$self->{empty_stack}});
    }
    return $result;
}


package TestMyQueueFromStacks;

my $m = MyQueueFromStacks->new;

use Test::More;

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

done_testing();
